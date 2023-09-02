import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {IPelicula} from "../interface/i-pelicula";

@Injectable({
  providedIn: 'root'
})
export class CargaPeliculasService {

  url = "http://localhost:3000/peliculas";
  urlIni = "http://localhost:3000/inicio";
  constructor(private http: HttpClient) { }

  getPeliculas(): Observable<IPelicula[]>{
    return this.http.get<IPelicula[]>(this.url)
  }

  removePelicula(id: number){
    this.http.delete(this.url+"/"+id).subscribe(
       error => console.log(error),
      () => console.log('Fin de observable')
    )
  }

  postPelicula(pelicula: IPelicula): Observable<IPelicula>{
    return this.http.post<IPelicula>(this.url, pelicula);
  }

  editPelicula(url: string,pelicula: IPelicula): Observable<IPelicula>{
    return this.http.put<IPelicula>(url, pelicula);
  }

  editPortada(id: any, datos: any):Observable<any>{
    return this.http.patch<any>(this.url+"/"+id, datos);
  }

}
