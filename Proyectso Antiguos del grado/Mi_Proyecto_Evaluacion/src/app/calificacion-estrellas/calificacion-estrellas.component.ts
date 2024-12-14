import {Component, Input} from '@angular/core';

@Component({
  selector: 'calificacion-estrellas',
  templateUrl: './calificacion-estrellas.component.html',
  styleUrls: ['./calificacion-estrellas.component.scss']
})
export class CalificacionEstrellasComponent {
  @Input() puntuacion: number | any;
}
