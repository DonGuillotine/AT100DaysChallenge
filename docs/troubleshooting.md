## Troubleshooting Guide

### 1. Books Not Processing / PDFs Are Not Being Processed

Possible Causes:

- PDFs not located in correct directory

- Incorrect BASE_DIR usage 

- File path mismatch
    
Verify path in command:

<pre>
books_dir = os.path.join(settings.BASE_DIR, 'lms_app', 'books')
</pre>
Make sure this directory exists and contains .pdf files.

### 2. Extracted text is empty

Possible Causes:
- Some PDFs are scanned images (not text-based)
- PyPDF2 cannot extract text from image PDFs

Fix:
 - Use OCR tools such as:
 - Tesseract
 - OCR-based preprocessing

### 3. Cohere Errors
- Authentication Error
  
    <pre>
    401 Unauthorized
    </pre>
    - Cause: Invalid or missing COHERE_API_KEY.

    - Fix: Ensure environment variable is set:
  
    <pre>
    echo $COHERE_API_KEY
    </pre>

- Rate Limit Error
  
    <pre>
    429 Too Many Requests
    </pre>
    
    - Cause: Cohere rate limit exceeded.
  
    - Fix:
        - Reduce batch size
        - Add retry logic
        - Check Cohere dashboard for quota limits

### 4. Pinecone Errors
- Index Not Found
  
    - Cause:
    Index does not exist.
  
    - Fix:
        - initialize_pinecone_index() should create it automatically.
        - Ensure PINECONE_ENVIRONMENT is correct.

- Dimension Mismatch
  
  If embedding model changes dimension, Pinecone index must match.

  Current dimension:
    
  <pre>
  dimension = 1024
  </pre>
    
  If model changes, update index accordingly.

### 5. Duplicate Book Processing
   
Processing logic checks:

<pre>
if created or not book.embedding_id:
</pre>

If embedding_id is empty, the book will reprocess.

Verify:
- embedding_id is properly saved
- Database is persistent

### 6. API Issues
- 404 on /api/books/

    Ensure:
    - Router is registered
    - URLs are included
    - DRF installed

- 500 Internal Server Error

    Check:
    - python manage.py runserver
    - Review traceback in console.

### 7. Chunking Issues
- Text Seems Truncated or Overlapping Incorrectly

    Chunking logic:
  
    <pre>
    chunk_size = 500
    overlap = 100
    </pre>
  
    Adjust values if:
    - Context too small
    - Overlap too large

### 8. Performance Issues
- Slow Processing
  
  - Possible reasons:

      -  Large PDFs
      - Large batch sizes
      - Network latency to Pinecone

  - Solutions:

      - Reduce batch_size
      - Process books asynchronously
      - Add logging to identify bottlenecks
