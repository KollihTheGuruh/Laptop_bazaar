// sw.js

self.addEventListener('install', (event) => {
    // Perform installation steps
    event.waitUntil(
        caches.open('my-cache').then((cache) => {
            return cache.addAll([
                '/static/css/styles.css',
                '/static/js/main.js',
                // Add other files you want to cache
            ]);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            // Cache hit - return response
            if (response) {
                return response;
            }

            // No cache match, fetch from the network
            return fetch(event.request);
        })
    );
});
