import goblin
from gremlin_python.process.traversal import Cardinality
from app import app
from properties import DateTime, Long


class AnnotatedVertexProperty(goblin.VertexProperty):

    notes = goblin.Property(goblin.String)
    datetime = goblin.Property(DateTime)


class House(goblin.Vertex):
    string_prop = AnnotatedVertexProperty(
        goblin.String, card=Cardinality.single)
    bool_prop = AnnotatedVertexProperty(
        goblin.Boolean, card=Cardinality.single)
    float_prop = AnnotatedVertexProperty(
        goblin.Float, card=Cardinality.single)
    int_prop = AnnotatedVertexProperty(
        goblin.Integer, card=Cardinality.single)
    long_prop = AnnotatedVertexProperty(Long, card=Cardinality.single)


class Structure(goblin.Vertex):
    struct_type = goblin.Property(goblin.String)


class BranchesTo(goblin.Edge):
    install_date = goblin.Property(DateTime)


app.register(House, Structure, BranchesTo)
