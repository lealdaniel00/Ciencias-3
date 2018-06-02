public class Estudiante{
       private string nombre;
       private string apellido;
       private string tipoIdentificacion;
       private int identificacion;
       private int codigo;
       private string correoInstitucional;
       private string correo;
      private Celular celular;
      private Direccion direccion;
       private string semestre;
      private Horario horario;

    public string getNombre(){
      return this.nombre;
    }
    public string getApellido(){
      return this.apellido;
    }
    public string getTipoidentificacion(){
      return this.tipoIdentificacion;
    }
    public integer getIdentificacion(){
      return this.identificacion;
    }
    public integer getCodigo(){
      return this.codigo;
    }
    public string getCorreoinstitucional(){
      return this.correoInstitucional;
    }
    public string getCorreo(){
      return this.correo;
    }
    public Celular getCelular(){
      return this.celular;
    }
    public Direccion getDireccion(){
      return this.direccion;
    }
    public string getSemestre(){
      return this.semestre;
    }
    public Horario getHorario(){
      return this.horario;
    }
    public void setNombre(string value){
      this.nombre = value;
    }
    public void setApellido(string value){
      this.apellido = value;
    }
    public void setTipoidentificacion(string value){
      this.tipoIdentificacion = value;
    }
    public void setIdentificacion(integer value){
      this.identificacion = value;
    }
    public void setCodigo(integer value){
      this.codigo = value;
    }
    public void setCorreoinstitucional(string value){
      this.correoInstitucional = value;
    }
    public void setCorreo(string value){
      this.correo = value;
    }
    public void setCelular(Celular value){
      this.celular = value;
    }
    public void setDireccion(Direccion value){
      this.direccion = value;
    }
    public void setSemestre(string value){
      this.semestre = value;
    }
    public void setHorario(Horario value){
      this.horario = value;
    }
}