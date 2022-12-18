import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'Lead Board';
  posts = [
    {
      title: 'number first',
      imageUrl: 'https://cdn-icons-png.flaticon.com/512/2519/2519215.png',
      username: 'ido',
      content: 'Good job you are awesome',
    },
    {
      title: 'number second',
      imageUrl: 'https://cdn-icons-png.flaticon.com/512/2460/2460850.png',
      username: 'avi',
      content: 'almost great',
    },
    {
      title: 'number third',
      imageUrl: 'https://cdn-icons-png.flaticon.com/512/1026/1026713.png',
      username: 'omer',
      content: 'keep going',
    },
  ];
}
