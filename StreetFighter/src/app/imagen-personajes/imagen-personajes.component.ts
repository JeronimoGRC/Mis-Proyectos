import {Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
import { ILuchador } from '../interfaces/i-luchador';
import {PersonajesService} from "../service_personajes/personajes.service";

@Component({
  selector: 'imagen-personajes, [imagen-personajes]',
  templateUrl: './imagen-personajes.component.html',
  styleUrls: ['./imagen-personajes.component.scss']
})
export class ImagenPersonajesComponent implements OnInit {
  @Input() personaje: ILuchador | any;
  @Input() indiceSeleccionado: number | any;
  @Input() numLuchador: number | any;
  @Output() luchadorSeleccionado = new EventEmitter<number>();
  hover = false;
  seleccionado = true;
  audio = new Audio("../assets/seleccionar.mp3");
  ngOnInit(): void {
  }

  reproducir(){
    this.audio.play();
  }

  alternar() {
    this.hover = !this.hover;
  }

  constructor() {
  }

  seleccionarLuchador() {
    // Se obtiene en la iteración del for en el area-seleccion
    if(this.numLuchador !== this.indiceSeleccionado){
      this.luchadorSeleccionado.emit(this.numLuchador);// lo emito al area seleccion
    }else{
      this.luchadorSeleccionado.emit(-1);
    }
  }

}
