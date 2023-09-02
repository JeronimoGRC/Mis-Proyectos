import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import { ILuchador } from '../interfaces/i-luchador';
import {PersonajesService} from "../service_personajes/personajes.service";

@Component({
  selector: 'atributos-luchador, [atributos-luchador]',
  templateUrl: './atributos-luchador.component.html',
  styleUrls: ['./atributos-luchador.component.scss']
})
export class AtributosLuchadorComponent{
  @Input() personajes: ILuchador | any;
  @Input() nombreLuchador: string | any;
  @Input() fuerza: string | any;
  @Input() vida: string | any;
  @Input() destreza: string | any;
  @Input() id: number | any;

  audio = new Audio("../assets/Fight.mp3");

  reproducir(){
    this.audio.play();
  }
}
