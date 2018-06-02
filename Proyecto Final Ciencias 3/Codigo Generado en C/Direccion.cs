public class Direccion{
       private string calle;
       private string barrio;
       private string ciudad;
       private string pais;

    public string getCalle(){
      return this.calle;
    }
    public string getBarrio(){
      return this.barrio;
    }
    public string getCiudad(){
      return this.ciudad;
    }
    public string getPais(){
      return this.pais;
    }
    public void setCalle(string value){
      this.calle = value;
    }
    public void setBarrio(string value){
      this.barrio = value;
    }
    public void setCiudad(string value){
      this.ciudad = value;
    }
    public void setPais(string value){
      this.pais = value;
    }
}