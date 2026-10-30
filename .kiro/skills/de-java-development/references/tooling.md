# Java Tooling

```bash
./mvnw -Dtest=FooTest test
./gradlew test --tests FooTest
./mvnw -q spotless:check   # if present
./gradlew check
```

Detect Checkstyle/SpotBugs/ErrorProne from the build and run what CI runs.
