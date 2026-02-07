import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 50,
  duration: '90s',
};

export default function () {
  http.get('http://localhost:8080/orders');
  sleep(1);
}
