from django.db import models

class CourseManager(models.Manager):
	"""
		Class para adicionar um select customizado do BD
		Utilizando o Manager do models
	"""

	def search(self, query):
		"""
			Metodo que filtra o que é digitado como query
			No name ou description
		"""
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | \
			models.Q(description__icontains=query)
		)

class Course(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição Simples', blank=True)
	about = models.TextField('Sobre o Curso', blank=True)
	start_date = models.DateField('Data de Inicio', null=True, blank=True)
	image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)

	upload_at = models.DateTimeField('Atualidado em', auto_now=True)

	objects = CourseManager()

	def __str__(self):
		return self.name

	@models.permalink
	def get_absolut_url(self):
		return ('courses:details', (), {'slug': self.slug})

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name']