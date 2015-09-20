# alfred-workflow-objectid

This Alfred Workflow plugin can parse MongoDB ObjectId objects, and extract information from it, e.g. timestamp, machine hash, etc. 

Attention: at present, only generation-time extraction is supported. Other ObjectId components will be supported in forthcoming releases.

## Usage

Use "oid" as the keyword. The argument can be either "gen", which will generate a fresh new ObjectId, or the hexademical string representation of an existing ObjectId.

## Screenshots

`oid gen`:

![oid gen](http://7af4ik.com1.z0.glb.clouddn.com/alfred/oid-gen.png?imageView2/2/w/600)

`oid 55fe9ea210114e253ddd0d63`

![oid 55fe9ea210114e253ddd0d63](http://7af4ik.com1.z0.glb.clouddn.com/alfred/oid-parser.png?imageView2/2/w/600)


