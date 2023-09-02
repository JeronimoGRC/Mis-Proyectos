import { Component } from '@angular/core';

@Component({
  selector: 'app-bienvenida',
  templateUrl: './bienvenida.component.html',
  styleUrls: ['./bienvenida.component.scss']
})
export class BienvenidaComponent {
  audio = new Audio("../assets/street-fighter-coin.mp3");

  reproducir(){
    this.audio.play();
  }
}
