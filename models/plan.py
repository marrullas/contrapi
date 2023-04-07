from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float,Text
from sqlalchemy.orm import relationship

from config.db_setup import Base

class Plan(Base):
    __tablename__ = 'plan'
    
    id = Column(Integer, primary_key=True)
    nombre_entidad = Column(String(50))
    nit = Column(String(12))
    nombre_representante_legal = Column(String(50))
    periodo_auditado = Column(Integer)
    anio_realizacion_auditoria = Column(Integer)
    nombre_informe = Column(String(50))
    modalidad_auditoria = Column(String(50))
    fecha_suscripcion_plan_mejoramiento = Column(Date)
    fecha_corte_avance = Column(Date)
    fecha_seguimiento_evaluacion = Column(Date)
    fecha_modificacion = Column(Date)
    
    detalles = relationship("DetallePlan", back_populates="plan")
    
class DetallePlan(Base):
    __tablename__ = 'detalle_plan'
    
    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey('plan.id'))
    numero_consecutivo_hallazgo = Column(Integer)
    codigo_hallazgo = Column(String(10))
    descripcion_hallazgo = Column(String(255))
    causa_hallazgo = Column(Text)
    efecto_hallazgo = Column(Text)
    accion_mejoramiento = Column(Text)
    objetivo = Column(Text)
    descripcion_metas = Column(Text)
    denominacion_unidad_medida_meta = Column(String(20))
    unidad_medida_meta = Column(String(10))
    avance_fisico_ejecucion_metas = Column(Float)
    porcentaje_avance_fisico_ejecucion_metas = Column(Float)
    fecha_inicio_metas = Column(Date)
    fecha_terminacion_metas = Column(Date)
    plazo_semanas_metas = Column(Integer)
    area_responsable = Column(String(50))
    
    plan = relationship("Plan", back_populates="detalles")
