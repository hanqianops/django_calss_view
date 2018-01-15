from django.db import models

class HostInfo(models.Model):
    hostname = models.CharField(max_length=30)
    ip = models.GenericIPAddressField(protocol='ipv4')
    cpu = models.IntegerField(blank=True,null=True)
    mem = models.CharField(max_length=30)
    deviceclass = models.CharField(max_length=30)

    class Meta:
        ordering = ("hostname",)
        permissions = (
            ("delete_host", "删除主机"),
            ("edis_host", "编辑主机"),
            ("create_host", "创建主机"),
        )

    def __str__(self):
        return self.hostname

