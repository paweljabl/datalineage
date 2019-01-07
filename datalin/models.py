from django.db import models

class Technology(models.Model):
    short_name = models.CharField(max_length=30, null=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    provider = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Entity(models.Model):
    short_name = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    is_storage = models.CharField(max_length=1)
    is_presentation = models.CharField(max_length=1)
    is_application = models.CharField(max_length=1, default='N')
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = (('short_name', 'technology'),)

    def __str__(self):
        # return '{0} - {1}'.format(self.technology.name, self.name)
        return '{0}'.format(self.name)

class Node(models.Model):
    name = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'entity'),)

    def __str__(self):
        return self.name

class Application(models.Model):
    node = models.OneToOneField(Node, on_delete=models.CASCADE, primary_key=True)
    owner_name = models.CharField(max_length=255, null=True)
    contact_email = models.EmailField(max_length=254, null=True)
    is_bi = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class Relation_Type(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Relation(models.Model):
    node_a = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="node_a")
    relation_type = models.ForeignKey(Relation_Type, on_delete=models.CASCADE)
    relation_level = models.IntegerField(default=1)
    node_b = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="node_b")

    class Meta:
        unique_together = (('node_a', 'relation_type', 'node_b'),)

    def __str__(self):
        return self.name