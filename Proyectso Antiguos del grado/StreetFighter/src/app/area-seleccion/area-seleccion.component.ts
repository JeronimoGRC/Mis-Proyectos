import { Component } from '@angular/core';
import { ILuchador } from '../interfaces/i-luchador';
import {PersonajesService} from "../service_personajes/personajes.service";

@Component({
  selector: 'area-seleccion',
  templateUrl: './area-seleccion.component.html',
  styleUrls: ['./area-seleccion.component.scss']
})
export class AreaSeleccionComponent {
    personajes: ILuchador[] = [];
    indiceSeleccionado = -1;// Valor por defecto

    constructor(private cargaPersonajes: PersonajesService) {
    }

    ngOnInit(){
      this.cargaPersonajes.getPersonajes().subscribe(
        listaPesonajes => {
          this.personajes = listaPesonajes;
        },
        error => console.log(error),
        () => console.log('Fin de observable')
      )
    }

}
