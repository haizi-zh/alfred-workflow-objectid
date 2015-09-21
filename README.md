# alfred-workflow-objectid

This Alfred Workflow plugin can parse MongoDB ObjectId objects, and extract some both basic and important information from them, e.g. generation timestamp, machine hash, etc. 

Attention: at present, only generation-time extraction is supported. Other ObjectId components will be supported in forthcoming releases.

## Usage

Use "oid" as the keyword. The argument can be either "gen", which will generate a fresh new ObjectId, or the hexademical string representation of an existing ObjectId.

## Screenshots

`oid gen`:

![oid gen](https://camo.githubusercontent.com/284b587223d8819d28ac672545896fd78c08f896/687474703a2f2f37616634696b2e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f616c667265642f6f69642d67656e2e706e673f696d61676556696577322f322f772f363030)

`oid 55fe9ea210114e253ddd0d63`

![oid 55fe9ea210114e253ddd0d63](https://camo.githubusercontent.com/da9ea94c54d7722ee844240cad09d5ae920cf951/687474703a2f2f37616634696b2e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f616c667265642f6f69642d7061727365722e706e673f696d61676556696577322f322f772f363030)


