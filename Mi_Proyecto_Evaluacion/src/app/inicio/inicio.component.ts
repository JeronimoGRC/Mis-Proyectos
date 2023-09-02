import { Component } from '@angular/core';
import {CargaPeliculasService} from "../service/carga-peliculas.service";
import {IPelicula} from "../interface/i-pelicula";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.component.html',
  styleUrls: ['./inicio.component.scss']
})
export class InicioComponent {
  peliculas: IPelicula[] = [];
  mostrada = false;
  editar = 'Editar';
  noEditar = 'No editar';

  constructor(private cargaPeliculas: CargaPeliculasService, private routes: Router,private route: ActivatedRoute) {
  }

  ngOnInit(){
    this.peliculas = this.route.snapshot.data['movies']
    /*this.cargaPeliculas.getPeliculas()*/
  }

  mostrarImagenes(){
    this.mostrada = !this.mostrada;
  }



}
