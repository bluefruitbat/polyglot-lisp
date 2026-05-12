FROM sbcl:2.4.0

# Self-contained: no shared volumes, no host mounts, no sibling refs
# Only explicit APIs (none here beyond standard SBCL)

WORKDIR /app

COPY definition.lisp runner.lisp /app/

CMD ["sbcl", "--script", "runner.lisp"]
