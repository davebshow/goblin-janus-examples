import goblin
from aiogremlin.gremlin_python import Cardinality
from app import app
from properties import DateTime, Long


class AnnotatedVertexProperty(goblin.VertexProperty):

    notes = goblin.Property(goblin.String)
    datetime = goblin.Property(DateTime)


class House(goblin.Vertex):
    string_prop = AnnotatedVertexProperty(
        goblin.String, card=Cardinality.list_)
    bool_prop = AnnotatedVertexProperty(
        goblin.Boolean, card=Cardinality.list_)
    float_prop = AnnotatedVertexProperty(
        goblin.Float, card=Cardinality.list_)
    int_prop = AnnotatedVertexProperty(
        goblin.Integer, card=Cardinality.list_)
    long_prop = AnnotatedVertexProperty(Long, card=Cardinality.list_)


class Structure(goblin.Vertex):
    struct_type = goblin.Property(goblin.String)


class BranchesTo(goblin.Edge):
    install_date = goblin.Property(DateTime)


app.register(House, Structure, BranchesTo)
