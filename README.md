# Introspector

A library for introspecting objects. It shows the attributes, methods and docstring.

```python
import introspector
import boto3


sts = boto3.client('sts')
introspector.dump(sts)
```
