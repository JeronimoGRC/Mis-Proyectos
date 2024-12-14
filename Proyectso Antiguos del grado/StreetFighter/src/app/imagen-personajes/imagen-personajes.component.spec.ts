import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImagenPersonajesComponent } from './imagen-personajes.component';

describe('ImagenPersonajesComponent', () => {
  let component: ImagenPersonajesComponent;
  let fixture: ComponentFixture<ImagenPersonajesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImagenPersonajesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ImagenPersonajesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
