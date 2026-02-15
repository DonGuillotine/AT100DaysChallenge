# AT100DaysChallenge API — Quickstart Guide

## 1. Base URL
<pre>
http://localhost:8000/
</pre>


## 2. List All Books
<pre>
curl -X GET http://localhost:8000/api/books/
</pre>

- Python Example:
<pre>
import requests

response = requests.get("http://localhost:8000/api/books/")
print(response.json())
</pre>

- C++ using libcurl:
    1. Install libcurl
         - Ubuntu/Debian
           <pre>
            sudo apt install libcurl4-openssl-dev
           </pre>
         - Mac
            <pre>
            brew install curl
            </pre>
    2. Example Code
    <pre>
    #include <iostream>
    #include <string>
    #include <curl/curl.h>
    
    static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
        ((std::string*)userp)->append((char*)contents, size * nmemb);
        return size * nmemb;
    }
    
    int main() {
        CURL* curl;
        CURLcode res;
        std::string readBuffer;
    
        curl = curl_easy_init();
        if(curl) {
            curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:8000/api/books/");
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
    
            // 🔐 Add Bearer token here
            struct curl_slist* headers = NULL;
            headers = curl_slist_append(headers, "Authorization: Bearer YOUR_TOKEN_HERE");
            headers = curl_slist_append(headers, "Content-Type: application/json");
    
            curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    
            res = curl_easy_perform(curl);
    
            if(res != CURLE_OK) {
                std::cerr << "curl_easy_perform() failed: "
                          << curl_easy_strerror(res) << std::endl;
            } else {
                std::cout << "Response:\n" << readBuffer << std::endl;
            }
    
            curl_slist_free_all(headers);  // 🧹 free header memory
            curl_easy_cleanup(curl);
        }
    
        return 0;
    }
    </pre>
      
    3. Compile
    <pre>
    g++ main.cpp -o get_books -lcurl
    </pre>
    4. Run:
    <pre>
    ./get_books
    </pre>

- JavaScript Example:
<pre>
fetch("http://localhost:8000/api/books/")
  .then(res => res.json())
  .then(console.log);
</pre>

## 3. Retrieve a Specific Book
<pre>
curl http://localhost:8000/api/books/1/
</pre>

## 4. Retrieve Book Chunks
<pre>
curl http://localhost:8000/api/books/1/chunks/
</pre>

## 5. Typical Response Format
<pre>
{
  
  "title": "Example Book",
  "author": "Author Name"
}
</pre>

