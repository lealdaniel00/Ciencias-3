public class Profesor{
       private string nombre;
       private string apellido;
       private string tipoIdentificacion;
       private int identificacion;
       private int codigo;
       private string correo;
      private Celular celular;
      private Direccion direccion;

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
    public string getCorreo(){
      return this.correo;
    }
    public Celular getCelular(){
      return this.celular;
    }
    public Direccion getDireccion(){
      return this.direccion;
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
    public void setCorreo(string value){
      this.correo = value;
    }
    public void setCelular(Celular value){
      this.celular = value;
    }
    public void setDireccion(Direccion value){
      this.direccion = value;
    }
}