# oracle_coding_exercise

This exercise runs using python 2.7.6 and does not require any dependencies.

To run:
  python main,py
  
Explanation of output:

```
*** Path from ENTRANCE to EXIT:
[u'ENTRANCE', u'EMPTY', u'MONSTER', u'EMPTY', u'TREASURE', u'EXIT']
```
The above is just finding a path from the entrance to the exit. It uses the map data provided by as a sample (see maps/sample.json).

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

