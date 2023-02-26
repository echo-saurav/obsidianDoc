---
layout: default
parent: android doc
title: Firestore
---
## Value type ordering

When a query involves a field with values of mixed types, Cloud Firestore uses a deterministic ordering based on the internal representations. The following list shows the order:

1.  Null values
2.  Boolean values
3.  Integer and floating-point values, sorted in numerical order
4.  Date values
5.  Text string values
6.  Byte values
7.  Cloud Firestore references
8.  Geographical point values
9.  Array values
10.  Map values