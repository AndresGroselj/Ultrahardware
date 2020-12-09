// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "ultrahardware-cache";
var filesToCache = [
    "/static/img/cart.png",
    "/static/img/close.png",
    "/static/img/loading.gif",
    "/static/img/logo.png",
    "/static/img/logo_160x160.png",
    "/static/img/logo_circle_turq.png",
    "/static/img/logo_circle_white.png",
    "/static/img/logo_UH.png",
    "/static/img/Logo_whiteBorder.png",
    "/static/img/next.png",
    "/static/img/prev.png",
    "/static/img/promo_1.png",
    "/static/img/promo_2.png",
    "/static/img/promo_3.png",
    "/static/img/promo_4.png",
    "/static/img/splash_640x1136.png",
    "/static/img/user_icon.png",
    "/static/css/cart.css",
    "/static/css/contact.css",
    "/static/css/index.css",
    "/static/css/location.css",
    "/static/css/login.css",
    "/static/css/product.css",
    "/static/css/productForm.css",
    "/static/css/productGalery.css",
    "/static/css/productPreview.css",
    "/static/css/product_list.css",
    "/static/css/sidebar.css",
    "/static/js/cart.js",
    "/static/js/contactValidator.js",
    "/static/js/productPreview.js",
    "/static/js/sidebar.js",
    "/static/controllers/productCardApiController.js",
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});