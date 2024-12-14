import { Injectable } from '@angular/core';
import {CargaPeliculasService} from "./carga-peliculas.service";
import {ActivatedRouteSnapshot, Router, RouterStateSnapshot} from "@angular/router";
import {catchError, Observable, of} from "rxjs";
import {IPelicula} from "../interface/i-pelicula";

@Injectable({
  providedIn: 'root'
})
export class ResolvePeliculaService {

  constructor(private cargaPeliculas: CargaPeliculasService, private route: Router) { }
  resolve(ruta: ActivatedRouteSnapshot, state: RouterStateSnapshot):Observable<IPelicula[]> | any{
    return this.cargaPeliculas.getPeliculas().pipe(
      catchError(err => {
        return of(null);
      })
    )
  }


}
