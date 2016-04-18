# oracle_coding_exercise

This exercise runs using python 2.7.6 and does not require any dependencies.

To run:
  python main.py [--graph-demo] [--tree-demo]
  
##Explanation of output:

###For the Graph Demo:

Shows the safest and most dangerous paths through the map:

--- Graph Demo ---

```
Safest path(s):
ENTRANCE
EMPTY
REWARD
REWARD
EMPTY
EXIT

Most dangerous path(s):
ENTRANCE
EMPTY
MONSTER
MONSTER
MONSTER
EMPTY
EXIT
```
There are potentially multiple safest / most dangerous paths - all paths with the lowest / highest (but same) cost will be shown.


### For the Tree Demo:
```
*** Path from ENTRANCE to EXIT:
[u'ENTRANCE', u'EMPTY', u'MONSTER', u'EMPTY', u'TREASURE', u'EXIT']
```
The above is just finding a path from the entrance to the exit. It uses the map data provided  as a sample (see maps/sample.json).

I have modelled the map as a binary tree, as this appeared to be enough to meet the spec (one entrance, 0-2 exits) and I could also represent the sample map using this. However I do believe that a more generic DAG (directed acyclic graph) would have allowed more freedom.

(I have not implemented it, but interesting things could be done when one encounters a monster or treasure.
Also - it currently only handles a single path.)

```
First serialized prefix string:
EMMT..._.T.._M_M..TX.....
Second serialized prefix string:
EMMT..._.T.._M_M..TX.....
They are equal.
and serialized out back to JSON again:
{"right": {"value": "EMPTY", "left": {"value": "MONSTER", "left": {"right": {"value": "TREASURE", "left": {"value": "EXIT"}}, "value": "EMPTY", "left": {"value": "MONSTER"}}}}, "value": "ENTRANCE", "left": {"right": {"right": {"value": "TREASURE"}, "value": "EMPTY"}, "value": "MONSTER", "left": {"value": "MONSTER", "left": {"value": "TREASURE"}}}}
```
The lines above are testing the serializers. I have implemented two - one that serializes / de-serializes from JSON, and another that uses my string based (but concise) format.
I ensure that the two schemes are compatible and that no data is lost over multiple reads and writes.

```

