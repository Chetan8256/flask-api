from config import ma, db

class Project(db.Model):
    __tablename__ = "Project"
    ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Technologies = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Project {self.Title}>'

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        load_instance = True
        sqla_session = db.session


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
