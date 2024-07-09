from gemini import Gemini
#
# cookies = {
#     "__Secure-1PSIDCC" : "AKEyXzVtC01Dh62UaU9kN8Bt691hjgqlP3uu7pce_Auta6boEoJWT860qJ0dJz4Xb94yoyxPg6k",
#     "__Secure-1PSID" : "g.a000lggIp90Mzf2y4am7OFLlLtvNRK-9A8OH2Dw2SGG8s3WrcmezYOMUK0nSQaVb-2xdGYQKiwACgYKAbsSARcSFQHGX2Mi_3m1IxGJvYFV2Hbj7IktfxoVAUF8yKqr3H53cz35LPIUwbsq9Seo0076",
#     "__Secure-1PSIDTS" : "sidts-CjIB4E2dkdBXRqxLGEzmMYrVTj4xTMowEYn-rMdEOEh3J2pxv-mx-yhnhdDjEZH2JMk-_xAA",
#     "NID" : "515=kF9fEXaYReX_LQzXq-egcyZWTwKYldogHzrz0jBy30wQq33GszsUSamByAtNnFifYGxY0QU4XBJd6rd_1rUK0w5db7AKCpAePTBSJefLdFClC_b9qGJFdkCXp-X8pxDx0GX4JXITUKo2oZnPVhc3NSjhgqvYO9uUTdAZvxHNLLBHW87y_7DDzpD6dTYI4TzWxYXLy_zdM8EC2weOJJmPwQw39b9a4HhqtGFreODr7OtAam7wDzkl6hDchzJGFgJlQrXX-i2eruZy0vWJH3SkGs2zfyjU8EWNk1yC6fkewWxx7r3l2mKewCf0bViPphKY1ij9LNLh8yAtUBm3G858U_mzOCGyVWCXn55TsyvQVSnViOrBBRaDFEpnZTpReZGJsUXn3Uys",
#     # Cookies may vary by account or region. Consider sending the entire cookie file.
#   }

# client = Gemini(cookies=cookies)

client = Gemini(cookie_fp="cookies_file.json")
prompt = "Hello, Gemini. Tell me about Large Language Models."
response = client.generate_content(prompt)
print(response.text)