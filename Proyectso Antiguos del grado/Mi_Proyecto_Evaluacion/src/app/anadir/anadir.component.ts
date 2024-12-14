import { Component } from '@angular/core';
import {CargaPeliculasService} from "../service/carga-peliculas.service";
import {IPelicula} from "../interface/i-pelicula";
import {FormBuilder, FormControl, FormGroup} from "@angular/forms";

@Component({
  selector: 'app-anadir',
  templateUrl: './anadir.component.html',
  styleUrls: ['./anadir.component.scss']
})
export class AnadirComponent {
  pelicula : IPelicula | any;
  string: string | any;
  img: string | any;

  constructor(private cargaPelicula: CargaPeliculasService, private formBuilder: FormBuilder) {
  }

  formulario = this.formBuilder.group({
    nombre: new FormControl(''),
    calificacion: new FormControl(''),
    genero: new FormControl(''),
    director: new FormControl(''),
    portada: new FormControl('')
  })

  cogerImagen(event: any){
    const reader = new FileReader();
    if(event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.img = reader.result as string;
      };
    }
  }

  anadir(){

    this.pelicula = {
      nombre: this.formulario.controls['nombre'].value,
      calificacion: this.formulario.controls['calificacion'].value,
      genero: this.formulario.controls['genero'].value,
      director: this.formulario.controls['director'].value,
      portada: this.img
    }

    this.cargaPelicula.postPelicula(this.pelicula).subscribe(
      error => console.log(error),
      () => console.log('Fin de observable'))

    alert("Se ha añadido una nueva película")
  }

}
