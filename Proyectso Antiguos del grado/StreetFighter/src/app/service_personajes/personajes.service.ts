import { Injectable } from '@angular/core';
import {ILuchador} from "../interfaces/i-luchador";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class PersonajesService {

  URLLuchadores = "http://localhost:3000/luchadores";

  constructor(private http: HttpClient) { }

  getPersonajes() :Observable<ILuchador[]>{
    return this.http.get<ILuchador[]>(this.URLLuchadores)
  }

}
