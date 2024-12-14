import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  audio = new Audio("../assets/seleccionar.mp3");

  reproducir(){
    this.audio.play();
  }
}
