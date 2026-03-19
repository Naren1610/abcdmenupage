const QRCode = require('qrcode');

const url = 'https://abcdmenupage-chi.vercel.app/';

QRCode.toFile('./qr/qrcode.png', url, {
  color: {
    dark: '#000',  // Black dots
    light: '#FFF' // Transparent background
  }
}, function (err) {
  if (err) throw err;
  console.log('QR code generated!');
});
