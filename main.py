import requests
import bs4

headers = {
    "accept-ch": "viewport-width,dpr,Sec-CH-Prefers-Color-Scheme,Sec-CH-UA-Full-Version-List,Sec-CH-UA-Platform-Version,Sec-CH-UA-Model",
    "accept-ch-lifetime": "4838400",
    "alt-svc": 'h3=":443"; ma=86400',
    "cache-control": "private, no-cache, no-store, must-revalidate",
    "content-encoding": "zstd",
    "content-security-policy": "default-src data: blob: 'self' https://*.fbsbx.com *.facebook.com *.fbcdn.net 'wasm-unsafe-eval';script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.google.com 127.0.0.1:* blob: data: 'self' connect.facebook.net 'wasm-unsafe-eval';style-src fonts.googleapis.com *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net wss://*.facebook.com:* wss://*.whatsapp.com:* wss://*.fbcdn.net attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' http://localhost:3103 wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d.facebook.com/ v.whatsapp.net *.fbsbx.com *.fb.com wss://web.whatsapp.com/ws/chat reg-e2ee.facebook.com cdn.fbsbx.com https://api.mapbox.com https://*.tiles.mapbox.com https://events.mapbox.com https://*.tenor.co;font-src data: *.gstatic.com *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net connect.facebook.net *.carriersignal.info blob: android-webview-video-poster: googleads.g.doubleclick.net www.googleadservices.com *.whatsapp.net *.fb.com *.oculuscdn.com *.tenor.co *.tenor.com *.giphy.com;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com data: *.tenor.co *.tenor.com https://*.giphy.com;frame-src *.doubleclick.net *.google.com *.facebook.com www.googleadservices.com *.fbsbx.com fbsbx.com data: www.instagram.com *.fbcdn.net https://paywithmybank.com/ https://sandbox.paywithmybank.com/;worker-src *.facebook.com/static_resources/webworker_v1/init_script/ *.facebook.com/static_resources/webworker/init_script/ *.facebook.com/static_resources/sharedworker/init_script/ *.facebook.com/static_resources/webworker/map_libre/ *.facebook.com/static_resources/webworker/map_libre_rtl/ *.facebook.com/sw/ *.facebook.com/sw;block-all-mixed-content;upgrade-insecure-requests;",
    "content-security-policy-report-only": "default-src data: blob: 'self' https://*.fbsbx.com *.facebook.com *.fbcdn.net 'wasm-unsafe-eval';script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.google.com 127.0.0.1:* blob: data: 'self' connect.facebook.net 'wasm-unsafe-eval';style-src fonts.googleapis.com *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net wss://*.facebook.com:* wss://*.whatsapp.com:* wss://*.fbcdn.net attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' http://localhost:3103 wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d.facebook.com/ v.whatsapp.net *.fbsbx.com *.fb.com wss://web.whatsapp.com/ws/chat reg-e2ee.facebook.com cdn.fbsbx.com https://api.mapbox.com https://*.tiles.mapbox.com https://events.mapbox.com https://*.tenor.co;font-src data: *.gstatic.com *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net connect.facebook.net *.carriersignal.info blob: android-webview-video-poster: googleads.g.doubleclick.net www.googleadservices.com *.whatsapp.net *.fb.com *.oculuscdn.com *.tenor.co *.tenor.com *.giphy.com;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com data: *.tenor.co *.tenor.com https://*.giphy.com;frame-src *.doubleclick.net *.google.com *.facebook.com www.googleadservices.com *.fbsbx.com fbsbx.com data: www.instagram.com *.fbcdn.net https://paywithmybank.com/ https://sandbox.paywithmybank.com/;worker-src *.facebook.com/static_resources/webworker_v1/init_script/ *.facebook.com/static_resources/webworker/init_script/ *.facebook.com/static_resources/sharedworker/init_script/ *.facebook.com/static_resources/webworker/map_libre/ *.facebook.com/static_resources/webworker/map_libre_rtl/ *.facebook.com/sw/ *.facebook.com/sw;block-all-mixed-content;report-uri https://www.facebook.com/csp/reporting/?minimize=0;",
    "content-type": 'text/html; charset="utf-8"',
    "cross-origin-embedder-policy-report-only": 'require-corp;report-to="coep_report"',
    "cross-origin-opener-policy": 'same-origin-allow-popups;report-to="coop_report"',
    "cross-origin-resource-policy": "same-origin",
    "date": "Sat, 23 Mar 2024 13:24:52 GMT",
    "document-policy": "force-load-at-top",
    "expires": "Sat, 01 Jan 2000 00:00:00 GMT",
    "origin-agent-cluster": "?0",
    "permissions-policy": 'accelerometer=(), ambient-light-sensor=(), autoplay=(), bluetooth=(), camera=(self), ch-device-memory=(), ch-save-data=(), ch-ua-arch=(), ch-ua-bitness=(), clipboard-read=(self), clipboard-write=(self), display-capture=(self), encrypted-media=(self), fullscreen=(self), gamepad=*, geolocation=(self), gyroscope=(), hid=(), idle-detection=(), keyboard-map=(), local-fonts=(), magnetometer=(), microphone=(self), midi=(), otp-credentials=(), payment=(), picture-in-picture=(self), publickey-credentials-get=(self), screen-wake-lock=(), serial=(), usb=(), window-management=(), xr-spatial-tracking=(self);report-to="permissions_policy"',
    "pragma": "no-cache",
    "priority": "u=1,i",
    "report-to": '{"max_age":2592000,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/browser_reporting\\/coop\\/?minimize=0"}],"group":"coop_report","include_subdomains":true}, {"max_age":86400,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/browser_reporting\\/coep\\/?minimize=0"}],"group":"coep_report"}, {"max_age":259200,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/ajax\\/comet_error_reports\\/?device_level=mod-high"}]}, {"max_age":21600,"endpoints":[{"url":"https:\\/\\/www.facebook.com\\/ajax\\/browser_error_reports\\/"}],"group":"permissions_policy"}',
    "reporting-endpoints": 'coop_report="https://www.facebook.com/browser_reporting/coop/?minimize=0", coep_report="https://www.facebook.com/browser_reporting/coep/?minimize=0", default="https://www.facebook.com/ajax/comet_error_reports/?device_level=mod-high", permissions_policy="https://www.facebook.com/ajax/browser_error_reports/"',
    "strict-transport-security": "max-age=15552000; preload",
    "vary": "Accept-Encoding",
    "x-content-type-options": "nosniff",
    "x-fb-connection-quality": "EXCELLENT; q=0.9, rtt=25, rtx=0, c=76, mss=1232, tbw=144213, tp=148, tpl=0, uplat=208, ullat=0",
    "x-fb-debug": "w/EX+8b2eSSgK67epSx70MpbDdL+nWRN9IBsxz+XyDLoWP1uJOLA5vWc6ZtbeB2nMdOYD502xDCINbIID1GeLQ==",
    "x-frame-options": "DENY",
    "x-xss-protection": "0",
}


s = requests.get(
    "https://www.facebook.com/itihadtahafuzfoundation/photos", headers=headers
)

b = bs4.BeautifulSoup(s.text, "html.parser")

print(b.find_all("img"))
