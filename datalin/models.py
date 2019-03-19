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
    weight = models.IntegerField(null=True)

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
    weight = models.IntegerField(null=True)

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
        return '{0} - {1}'.format(self.node_a.display_name, self.node_b.display_name)

class Application_Load(models.Model):
    name = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=100, null=True)
    entity = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    owner_name = models.CharField(max_length=255, null=True)
    contact_email = models.CharField(max_length=255, null=True)
    is_bi = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.name

class Load_Log(models.Model):
    load_id = models.IntegerField()
    table_name = models.CharField(max_length=255)
    sql_operation = models.CharField(max_length=100, null=True)
    start_timestamp = models.DateTimeField()
    duration_seconds = models.IntegerField(null=True)
    row_count = models.IntegerField(null=True)
    success_flag = models.CharField(max_length=1, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.table_name, self.start_timestamp)

class Node_Load(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    entity = models.CharField(max_length=100, null=True)
    technology = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Relation_Load(models.Model):
    node_a = models.CharField(max_length=255)
    relation_type = models.CharField(max_length=30)
    relation_level = models.IntegerField(null=True)
    node_b = models.CharField(max_length=255)

    def __str__(self):
        return '{0} - {1}'.format(self.node_a, self.node_b)

class Full_Load(models.Model):
    a_name = models.CharField(max_length=255)
    a_display_name = models.CharField(max_length=100, null=True)
    a_description = models.CharField(max_length=500, null=True)
    a_entity = models.CharField(max_length=100, null=True)
    a_technology = models.CharField(max_length=100, null=True)
    relation_type = models.CharField(max_length=30)
    relation_level = models.IntegerField(null=True)
    b_name = models.CharField(max_length=255)
    b_display_name = models.CharField(max_length=100, null=True)
    b_description = models.CharField(max_length=500, null=True)
    b_entity = models.CharField(max_length=100, null=True)
    b_technology = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name