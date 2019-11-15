// Databricks notebook source
import org.apache.spark._
import org.apache.spark.graphx._
// To make some of the examples work we will also need RDD
import org.apache.spark.rdd.RDD

// COMMAND ----------

// Assume the SparkContext has already been constructed

//val sc: SparkContext
// Create an RDD for the vertices
val users: RDD[(VertexId, (String, String))] =
  sc.parallelize(Array((3L, ("rxin", "student")), (7L, ("jgonzal", "postdoc")),
                       (5L, ("franklin", "prof")), (2L, ("istoica", "prof"))))
// Create an RDD for edges
val relationships: RDD[Edge[String]] =
  sc.parallelize(Array(Edge(3L, 7L, "collab"),    Edge(5L, 3L, "advisor"),
                       Edge(2L, 5L, "colleague"), Edge(5L, 7L, "pi")))
// Define a default user in case there are relationship with missing user
val defaultUser = ("John Doe", "Missing")
// Build the initial Graph
val graph = Graph(users, relationships, defaultUser)

// COMMAND ----------

graph
  .groupEdges((edge1, edge2) => edge1 + edge2)
  .triplets
  .sortBy(_.attr, ascending=false)
  .map(triplet => 
    "There were " + triplet.attr.toString + " trips from " + triplet.srcAttr + " to " + triplet.dstAttr + ".")
  .take(10)
  .foreach(println)

// COMMAND ----------

//val vertex_file = sqlContext.read.format("com.databricks.spark.csv").option("delimiter", ",").load("csvfile.csv")
val vertex_data = sqlContext.sql("select * from vertex_list_csv")
val edge_data = sqlContext.sql("select * from edge_list_csv")

// COMMAND ----------

val tableEdges:RDD[Edge[String]] = edge_data
  .rdd
  //.distinct() // helps filter out duplicate trips
  .map(row => Edge(row(0).asInstanceOf[Number].longValue, row(1).asInstanceOf[Number].longValue, row(2).asInstanceOf[String]))

val tableVertices:RDD[(VertexId, String)] = vertex_data
  .rdd
  .map(row => (row(0).asInstanceOf[Number].longValue, row(1).asInstanceOf[String]))

val defaultlink =("Missing table")

val graph = Graph(tableVertices, tableEdges, defaultlink)

// COMMAND ----------

print("Total number of tables: "+graph.numVertices+"\n")
print("Total number of relations: "+graph.numEdges+"\n")
//sanity check
println("Total Number of tables in Original Data: " + vertex_data.count)


// COMMAND ----------

graph
  .groupEdges((edge1, edge2) => edge1 + edge2)
  .triplets
  .sortBy(_.attr, ascending=false)
  .map(triplet => 
    "The relation is " + triplet.attr.toString + " between " + triplet.srcAttr + " and " + triplet.dstAttr + ".")
  .take(10000)
  .foreach(println)

// COMMAND ----------

//computing page rank for top 10 tables
val ranks = graph.pageRank(0.0001).vertices
ranks
  .join(tableVertices)
  .sortBy(_._2._1, ascending=false) // sort by the rank
  .take(10) // get the top 10
  .foreach(x => println(x._2._2))

// COMMAND ----------

//calculating number of links in top 10 tables
//inward links
graph
  .inDegrees // computes in Degrees
  .join(tableVertices)
  .sortBy(_._2._1, ascending=false)
  .take(10)
  .foreach(x => println(x._2._2 + " has " + x._2._1 + " in degrees."))


//outward links
graph
  .outDegrees // computes in Degrees
  .join(tableVertices)
  .sortBy(_._2._1, ascending=false)
  .take(10)
  .foreach(x => println(x._2._2 + " has " + x._2._1 + " out degrees."))

// COMMAND ----------

import org.apache.spark.graphx._
import scala.reflect.ClassTag
def drawGraph[VD:ClassTag,ED:ClassTag](g:Graph[VD,ED]) = {

val u = java.util.UUID.randomUUID
val v = graph.vertices.collect.map(_._1)
println("""<!DOCTYPE html>
     <html lang="en">
     <head>
     <meta charset="utf-8">
     <title>Graph</title>
<div id='a""" + u + """' style='width:960px; height:500px'></div> 
<style>
.node circle { fill: gray; }
.node text { font: 10px sans-serif;
     text-anchor: middle;
     fill: white; }
line.link { stroke: gray;
    stroke-width: 1.5px; }
</style>
<script src="//d3js.org/d3.v3.min.js"></script>
<script>
.var width = 960, height = 500;
var svg = d3.select("#a""" + u + """").append("svg")
.attr("width", width).attr("height", height);
var nodes = [""" + v.map("{id:" + _ + "}").mkString(",") + """];
var links = [""" + graph.edges.collect.map(
e => "{source:nodes[" + v.indexWhere(_ == e.srcId) + 
"],target:nodes[" +
v.indexWhere(_ == e.dstId) + "]}").mkString(",") + """];
var link = svg.selectAll(".link").data(links);
link.enter().insert("line", ".node").attr("class", "link");
var node = svg.selectAll(".node").data(nodes);
var nodeEnter = node.enter().append("g").attr("class", "node")
nodeEnter.append("circle").attr("r", 8);
nodeEnter.append("text").attr("dy", "0.35em")
 .text(function(d) { return d.id; });
d3.layout.force().linkDistance(50).charge(-200).chargeDistance(300)
.friction(0.95).linkStrength(0.5).size([width, height])
.on("tick", function() {
link.attr("x1", function(d) { return d.source.x; })
  .attr("y1", function(d) { return d.source.y; })
  .attr("x2", function(d) { return d.target.x; })
  .attr("y2", function(d) { return d.target.y; });
node.attr("transform", function(d) {
return "translate(" + d.x + "," + d.y + ")";
});
}).nodes(nodes).links(links).start();
</script>
</body>
    </html>
 """)
 }

// COMMAND ----------

drawGraph(graph)

// COMMAND ----------


