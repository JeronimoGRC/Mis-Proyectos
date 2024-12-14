import { Component } from '@angular/core';
import {IPelicula} from "../interface/i-pelicula";
import {CargaPeliculasService} from "../service/carga-peliculas.service";
import {FormBuilder, FormControl} from "@angular/forms";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-editar',
  templateUrl: './editar.component.html',
  styleUrls: ['./editar.component.scss']
})
export class EditarComponent {
  pelicula : IPelicula | any;
  idPelicula: number = 0;
  url = "http://localhost:3000/peliculas";
  string: string | any;
  img: string | any;

  constructor(private cargaPelicula: CargaPeliculasService, private formBuilder: FormBuilder, private route: ActivatedRoute) {
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

  editar(){

    this.idPelicula = this.route.snapshot.params['id'];
    this.url += "/" + this.idPelicula;

    this.pelicula = {
      nombre: this.formulario.controls['nombre'].value,
      calificacion: this.formulario.controls['calificacion'].value,
      genero: this.formulario.controls['genero'].value,
      director: this.formulario.controls['director'].value,
      portada: this.img
    }

    this.cargaPelicula.editPelicula(this.url,this.pelicula).subscribe(
      error => console.log(error),
      () => console.log('Fin de observable')
    )

    alert("Edicion de pelicula completada")
  }
}




  