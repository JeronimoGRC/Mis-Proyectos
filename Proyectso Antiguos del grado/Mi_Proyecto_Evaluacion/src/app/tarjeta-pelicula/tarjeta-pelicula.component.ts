import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {IPelicula} from "../interface/i-pelicula";
import {CargaPeliculasService} from "../service/carga-peliculas.service";
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {HttpClient} from "@angular/common/http";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'tarjeta-pelicula, [tarjeta-pelicula]',
  templateUrl: './tarjeta-pelicula.component.html',
  styleUrls: ['./tarjeta-pelicula.component.scss']
})
export class TarjetaPeliculaComponent implements OnInit{
  @Input() pelicula: IPelicula[] | any;
  @Input() editar: boolean | any;

  imageSrc: string = '';

  myForm = new FormGroup({
    file: new FormControl('', [Validators.required]),
    fileSource: new FormControl('', [Validators.required])
  });

  constructor(private peliculasService: CargaPeliculasService,private http: HttpClient, private routes: Router,private route: ActivatedRoute) {}

  ngOnInit(){
  }

  cambiar(event: any){
    const reader = new FileReader();
    if(event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.imageSrc = reader.result as string;
      };
    }
  }

  enviar(){
    let data = {
      portada: this.imageSrc
    }

    this.peliculasService.editPortada(this.pelicula.id, data).subscribe(() =>{},
      error => console.log(error)
      )
    window.location.reload();

  }

  borrar(){
    this.peliculasService.removePelicula(this.pelicula.id)
    window.location.reload();
  }
}
