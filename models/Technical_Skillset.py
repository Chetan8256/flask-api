from config import ma, db

class Technical_Skillset(db.Model):
    __tablename__ = "Technical_Skillset"
    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('Project.ID'), nullable=False)
    Frontend = db.Column(db.String(200), nullable=True)
    Backend = db.Column(db.String(200), nullable=True)
    Databases = db.Column(db.String(100), nullable=True)
    Infrastructre = db.Column(db.String(200), nullable=True)


    def __repr__(self):
        return f'<Project {self.ID}>'
    
class Technical_SkillsetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Technical_Skillset
        load_instance = True
        sqla_session = db.session


technical_skillet_schema = Technical_SkillsetSchema()
technical_skillets_schema = Technical_SkillsetSchema(many=True)