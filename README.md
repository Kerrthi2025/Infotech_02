# Infotech_02
**Pixel Manipulation for Image Encryption**
Pixel manipulation for image encryption includes the process of modifying the RGB values of each pixel in an image using cryptographic algorithms to render the image not readble without proper decryption. During encryption, the RGB values of pixels are altered in a controlled manner to obscure the image's content while maintaining its visual appearance. Decryption reverses this process, restoring the original image by applying the inverse operations with the correct decryption key or algorithm. While pixel manipulation serves as a fundamental technique for image encryption, it's important to recognize its limitations in providing robust security against sophisticated attacks, making it more suitable for educational or basic encryption purposes within larger security frameworks.


Encryption
It is nothing but a simple process in which we convert our data or information into secret code to prevent it from unauthorized access and keep it private and secure.

First, we will select an image, and then we will convert that image into a byte array due to which the image data will be totally converted into numeric form, and then we can easily apply the XOR operation to it. Now, whenever we will apply the XOR function on each value of the byte array then the data will be changed due to which we will be unable to access it. But we should remember one thing here our encryption key plays a very important role without that key we can not decrypt our image. It acts as a password to decrypt it.
