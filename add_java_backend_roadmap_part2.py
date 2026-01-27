"""
Add Java Backend Roadmap - Part 2 (Stages 3, 4, 5)
"""

import os
import django
import sys

sys.path.append('/Users/saitejakaki/Divakar/devaproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roadmap99.settings')
django.setup()

from core.models import Roadmap, Stage, Topic

def add_remaining_stages():
    """Add stages 3, 4, and 5 to Java Backend roadmap"""
    
    roadmap = Roadmap.objects.get(slug='java-backend-development')
    print(f"Adding stages to: {roadmap.title}")
    
    # Stage 3: Spring & Spring Boot
    stage3 = Stage.objects.create(
        roadmap=roadmap,
        title='Spring & Spring Boot Basics',
        description='Build real backend services with Spring Boot - REST APIs, dependency injection, and more',
        order=3,
        is_free=False
    )
    
    stage3_topics = [
        {
            'title': 'Why Spring Framework Exists',
            'content': '''# Why Spring Framework Exists

## The Problem Spring Solves

Before Spring, Java backend development was:
- **Complex**: Too much boilerplate code
- **Tightly Coupled**: Hard to test and maintain
- **Configuration Hell**: XML files everywhere
- **Slow Development**: Manual object creation and wiring

## What is Spring?

Spring is a **framework** that simplifies Java backend development by:
1. Managing object creation (Dependency Injection)
2. Providing ready-to-use components
3. Handling common backend tasks
4. Making code testable and maintainable

## Spring Boot vs Spring Framework

**Spring Framework**: Core features (DI, AOP, etc.)
**Spring Boot**: Spring + Auto-configuration + Embedded server

Spring Boot = Spring Framework made easy!

## Why Companies Use Spring Boot

- **Netflix, Amazon, LinkedIn** use it
- Rapid development (build APIs in minutes)
- Production-ready features (monitoring, security)
- Huge ecosystem and community
- Industry standard for Java backend
''',
            'order': 1
        },
        {
            'title': 'Dependency Injection Concept',
            'content': '''# Dependency Injection (DI)

## The Problem

```java
// Without DI (tightly coupled)
public class UserService {
    private UserRepository repo = new UserRepository();
    // Problem: UserService creates its own dependency
    // Hard to test, hard to change implementation
}
```

## The Solution: Dependency Injection

```java
// With DI (loosely coupled)
@Service
public class UserService {
    private final UserRepository repo;
    
    @Autowired  // Spring injects dependency
    public UserService(UserRepository repo) {
        this.repo = repo;
    }
}
```

**Benefits:**
- Easy to test (inject mock repository)
- Easy to swap implementations
- Spring manages object lifecycle

## Spring Annotations

- `@Component`: Generic Spring-managed bean
- `@Service`: Business logic layer
- `@Repository`: Data access layer
- `@Controller` / `@RestController`: Web layer
- `@Autowired`: Inject dependencies
''',
            'order': 2
        },
        {
            'title': 'Spring Boot Project Setup',
            'content': '''# Spring Boot Project Setup

## Create New Project

**Option 1: Spring Initializr (start.spring.io)**
1. Go to https://start.spring.io
2. Select: Maven, Java, Spring Boot 3.x
3. Add dependencies: Spring Web, Spring Data JPA, MySQL Driver
4. Generate and download ZIP

**Option 2: IntelliJ IDEA**
File → New → Project → Spring Initializr

## Project Structure

```
project/
├── src/main/java/com/example/demo/
│   ├── DemoApplication.java
│   ├── controller/
│   ├── service/
│   ├── repository/
│   └── model/
├── src/main/resources/
│   └── application.properties
└── pom.xml
```

## Run Application

```bash
mvn spring-boot:run
# or
./mvnw spring-boot:run
```

Access: http://localhost:8080
''',
            'order': 3
        },
        {
            'title': 'Creating REST APIs',
            'content': '''# Creating REST APIs

## Simple REST Controller

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping
    public List<User> getAllUsers() {
        return Arrays.asList(
            new User(1L, "John"),
            new User(2L, "Jane")
        );
    }
    
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        return new User(id, "John");
    }
    
    @PostMapping
    public User createUser(@RequestBody User user) {
        // Save user logic
        return user;
    }
    
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        return user;
    }
    
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        // Delete logic
    }
}
```

## Testing APIs

```bash
# GET request
curl http://localhost:8080/api/users

# POST request
curl -X POST http://localhost:8080/api/users \\
  -H "Content-Type: application/json" \\
  -d '{"name":"John","email":"john@example.com"}'
```
''',
            'order': 4
        },
        {
            'title': 'Handling HTTP Requests & Responses',
            'content': '''# HTTP Request & Response Handling

## Request Parameters

```java
@RestController
public class ProductController {
    
    // Query params: /products?category=electronics&minPrice=1000
    @GetMapping("/products")
    public List<Product> search(
        @RequestParam String category,
        @RequestParam(required = false) Double minPrice
    ) {
        return productService.search(category, minPrice);
    }
    
    // Path variable: /products/123
    @GetMapping("/products/{id}")
    public Product getProduct(@PathVariable Long id) {
        return productService.findById(id);
    }
    
    // Request body
    @PostMapping("/products")
    public Product create(@RequestBody Product product) {
        return productService.save(product);
    }
}
```

## Response Status Codes

```java
@PostMapping("/users")
public ResponseEntity<User> createUser(@RequestBody User user) {
    User saved = userService.save(user);
    return ResponseEntity
        .status(HttpStatus.CREATED)
        .body(saved);
}

@GetMapping("/users/{id}")
public ResponseEntity<User> getUser(@PathVariable Long id) {
    User user = userService.findById(id);
    if (user == null) {
        return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(user);
}
```

## Response Headers

```java
@GetMapping("/download")
public ResponseEntity<byte[]> download() {
    HttpHeaders headers = new HttpHeaders();
    headers.setContentType(MediaType.APPLICATION_PDF);
    headers.setContentDispositionFormData("attachment", "file.pdf");
    
    return ResponseEntity.ok()
        .headers(headers)
        .body(fileData);
}
```
''',
            'order': 5
        }
    ]
    
    for topic_data in stage3_topics:
        Topic.objects.create(stage=stage3, **topic_data)
    
    print(f"✅ Stage 3: {stage3.title} - {len(stage3_topics)} topics")
    
    # Stage 4: Database & API Integration
    stage4 = Stage.objects.create(
        roadmap=roadmap,
        title='Database & API Integration',
        description='Connect backend to databases, perform CRUD operations, and integrate with external APIs',
        order=4,
        is_free=False
    )
    
    stage4_topics = [
        {
            'title': 'SQL Basics for Backend',
            'content': '''# SQL Basics

## Essential SQL Commands

```sql
-- CREATE TABLE
CREATE TABLE users (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- INSERT
INSERT INTO users (username, email, password)
VALUES ('john_doe', 'john@example.com', 'hashed_password');

-- SELECT
SELECT * FROM users;
SELECT id, username FROM users WHERE email = 'john@example.com';

-- UPDATE
UPDATE users SET email = 'newemail@example.com' WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;
```

## Relationships

```sql
-- One-to-Many: User has many Posts
CREATE TABLE posts (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200),
    content TEXT,
    user_id BIGINT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Query with JOIN
SELECT users.username, posts.title
FROM users
INNER JOIN posts ON users.id = posts.user_id;
```
''',
            'order': 1
        },
        {
            'title': 'Connecting Java to Database',
            'content': '''# Database Connection

## application.properties

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

## Entity Class

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(unique = true, nullable = false)
    private String username;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    private String password;
    
    // Getters and Setters
}
```

## Repository Interface

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    boolean existsByEmail(String email);
}
```

## Service Layer

```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    
    public User createUser(User user) {
        if (userRepository.existsByEmail(user.getEmail())) {
            throw new EmailExistsException("Email already registered");
        }
        return userRepository.save(user);
    }
    
    public User findById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
    }
}
```
''',
            'order': 2
        },
        {
            'title': 'CRUD Operations',
            'content': '''# CRUD Operations

## Complete CRUD Example

```java
@RestController
@RequestMapping("/api/products")
public class ProductController {
    
    @Autowired
    private ProductService productService;
    
    // CREATE
    @PostMapping
    public ResponseEntity<Product> create(@RequestBody Product product) {
        Product saved = productService.save(product);
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);
    }
    
    // READ (All)
    @GetMapping
    public List<Product> getAll() {
        return productService.findAll();
    }
    
    // READ (One)
    @GetMapping("/{id}")
    public ResponseEntity<Product> getById(@PathVariable Long id) {
        Product product = productService.findById(id);
        return ResponseEntity.ok(product);
    }
    
    // UPDATE
    @PutMapping("/{id}")
    public ResponseEntity<Product> update(
        @PathVariable Long id,
        @RequestBody Product product
    ) {
        Product updated = productService.update(id, product);
        return ResponseEntity.ok(updated);
    }
    
    // DELETE
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        productService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
```

## Service Implementation

```java
@Service
public class ProductService {
    @Autowired
    private ProductRepository repository;
    
    public Product save(Product product) {
        return repository.save(product);
    }
    
    public List<Product> findAll() {
        return repository.findAll();
    }
    
    public Product findById(Long id) {
        return repository.findById(id)
            .orElseThrow(() -> new ProductNotFoundException("Product not found"));
    }
    
    public Product update(Long id, Product product) {
        Product existing = findById(id);
        existing.setName(product.getName());
        existing.setPrice(product.getPrice());
        return repository.save(existing);
    }
    
    public void delete(Long id) {
        repository.deleteById(id);
    }
}
```
''',
            'order': 3
        },
        {
            'title': 'JPA & Hibernate Basics',
            'content': '''# JPA & Hibernate

## What is ORM?

**Object-Relational Mapping** converts Java objects to database tables automatically.

Without ORM:
```java
// Manual SQL
String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setString(1, user.getName());
stmt.setString(2, user.getEmail());
stmt.executeUpdate();
```

With ORM (JPA/Hibernate):
```java
userRepository.save(user);  // That's it!
```

## Entity Relationships

```java
// One-to-Many
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
    private List<Post> posts;
}

@Entity
public class Post {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;
}
```

## Custom Queries

```java
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
    
    // Method name query
    List<Product> findByPriceGreaterThan(Double price);
    List<Product> findByNameContaining(String keyword);
    
    // JPQL
    @Query("SELECT p FROM Product p WHERE p.price BETWEEN :min AND :max")
    List<Product> findByPriceRange(@Param("min") Double min, @Param("max") Double max);
    
    // Native SQL
    @Query(value = "SELECT * FROM products WHERE price > ?1", nativeQuery = true)
    List<Product> findExpensiveProducts(Double price);
}
```
''',
            'order': 4
        },
        {
            'title': 'Data Validation',
            'content': '''# Data Validation

## Bean Validation Annotations

```java
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @NotBlank(message = "Username is required")
    @Size(min = 3, max = 50, message = "Username must be 3-50 characters")
    private String username;
    
    @Email(message = "Invalid email format")
    @NotBlank(message = "Email is required")
    private String email;
    
    @Size(min = 8, message = "Password must be at least 8 characters")
    private String password;
    
    @Min(value = 18, message = "Age must be at least 18")
    private Integer age;
    
    @Pattern(regexp = "^\\+?[1-9]\\d{1,14}$", message = "Invalid phone number")
    private String phone;
}
```

## Controller Validation

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @PostMapping
    public ResponseEntity<?> createUser(@Valid @RequestBody User user) {
        // @Valid triggers validation
        // If validation fails, returns 400 Bad Request
        User saved = userService.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);
    }
}
```

## Global Exception Handler

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidationErrors(
        MethodArgumentNotValidException ex
    ) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error -> 
            errors.put(error.getField(), error.getDefaultMessage())
        );
        return ResponseEntity.badRequest().body(errors);
    }
}
```

## Custom Validator

```java
@Target({ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = UniqueEmailValidator.class)
public @interface UniqueEmail {
    String message() default "Email already exists";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

public class UniqueEmailValidator implements ConstraintValidator<UniqueEmail, String> {
    @Autowired
    private UserRepository userRepository;
    
    @Override
    public boolean isValid(String email, ConstraintValidatorContext context) {
        return !userRepository.existsByEmail(email);
    }
}
```
''',
            'order': 5
        }
    ]
    
    for topic_data in stage4_topics:
        Topic.objects.create(stage=stage4, **topic_data)
    
    print(f"✅ Stage 4: {stage4.title} - {len(stage4_topics)} topics")
    
    # Stage 5: Industry-Ready Skills
    stage5 = Stage.objects.create(
        roadmap=roadmap,
        title='Industry-Ready Backend Skills',
        description='Master authentication, security, deployment, and best practices to become job-ready',
        order=5,
        is_free=False
    )
    
    stage5_topics = [
        {
            'title': 'Authentication & Authorization',
            'content': '''# Authentication & Authorization

## Authentication (Who are you?)

**Basic Authentication Flow:**
1. User enters email/password
2. Backend checks credentials
3. Returns token (JWT)
4. User sends token with each request

## Password Hashing

```java
@Configuration
public class SecurityConfig {
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}

@Service
public class UserService {
    @Autowired
    private PasswordEncoder passwordEncoder;
    
    public User register(UserDTO dto) {
        User user = new User();
        user.setEmail(dto.getEmail());
        // Hash password before saving
        user.setPassword(passwordEncoder.encode(dto.getPassword()));
        return userRepository.save(user);
    }
    
    public boolean login(String email, String password) {
        User user = userRepository.findByEmail(email)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
        
        // Compare plain password with hashed password
        return passwordEncoder.matches(password, user.getPassword());
    }
}
```

## Authorization (What can you do?)

```java
@Entity
public class User {
    @Enumerated(EnumType.STRING)
    private Role role;  // USER, ADMIN, MODERATOR
}

// Check role in controller
@PreAuthorize("hasRole('ADMIN')")
@DeleteMapping("/users/{id}")
public void deleteUser(@PathVariable Long id) {
    userService.delete(id);
}
```

## JWT Token (Simple Example)

```java
public class JwtUtil {
    private String SECRET_KEY = "your-secret-key";
    
    public String generateToken(String email) {
        return Jwts.builder()
            .setSubject(email)
            .setIssuedAt(new Date())
            .setExpiration(new Date(System.currentTimeMillis() + 86400000)) // 1 day
            .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
            .compact();
    }
    
    public String extractEmail(String token) {
        return Jwts.parser()
            .setSigningKey(SECRET_KEY)
            .parseClaimsJws(token)
            .getBody()
            .getSubject();
    }
}
```
''',
            'order': 1
        },
        {
            'title': 'Backend Security Concepts',
            'content': '''# Backend Security

## Common Vulnerabilities

### 1. SQL Injection

```java
// ❌ Bad (vulnerable)
String sql = "SELECT * FROM users WHERE email = '" + email + "'";
// Attacker can inject: ' OR '1'='1

// ✅ Good (safe)
@Query("SELECT u FROM User u WHERE u.email = :email")  // Parameterized
User findByEmail(@Param("email") String email);
```

### 2. XSS (Cross-Site Scripting)

```java
// Sanitize user input
import org.springframework.web.util.HtmlUtils;

String sanitized = HtmlUtils.htmlEscape(userInput);
```

### 3. Password Security

```java
// ❌ Never store plain passwords
user.setPassword(password);

// ✅ Always hash
user.setPassword(passwordEncoder.encode(password));
```

## CORS Configuration

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
            .allowedOrigins("http://localhost:3000")  // Frontend URL
            .allowedMethods("GET", "POST", "PUT", "DELETE")
            .allowedHeaders("*")
            .allowCredentials(true);
    }
}
```

## Input Validation

```java
// Always validate user input
@PostMapping("/transfer")
public void transfer(@Valid @RequestBody TransferRequest request) {
    if (request.getAmount() <= 0) {
        throw new InvalidAmountException("Amount must be positive");
    }
    if (request.getAmount() > 100000) {
        throw new LimitExceededException("Daily limit exceeded");
    }
    transferService.execute(request);
}
```

## Rate Limiting

```java
// Prevent brute force attacks
@GetMapping("/login")
@RateLimiter(name = "loginLimiter")
public ResponseEntity<String> login(@RequestBody LoginDTO dto) {
    // Max 5 login attempts per minute
    return authService.login(dto);
}
```
''',
            'order': 2
        },
        {
            'title': 'API Best Practices',
            'content': '''# API Best Practices

## 1. RESTful Design

```java
// ✅ Good
GET    /api/users           - Get all users
GET    /api/users/123       - Get user by ID
POST   /api/users           - Create user
PUT    /api/users/123       - Update user
DELETE /api/users/123       - Delete user

// ❌ Bad
GET /api/getAllUsers
POST /api/createNewUser
GET /api/getUserById?id=123
```

## 2. Proper HTTP Status Codes

```java
// 200 OK - Success
return ResponseEntity.ok(data);

// 201 Created - Resource created
return ResponseEntity.status(HttpStatus.CREATED).body(newUser);

// 204 No Content - Success but no data
return ResponseEntity.noContent().build();

// 400 Bad Request - Invalid input
return ResponseEntity.badRequest().body(errors);

// 401 Unauthorized - Not authenticated
return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();

// 403 Forbidden - Authenticated but no permission
return ResponseEntity.status(HttpStatus.FORBIDDEN).build();

// 404 Not Found
return ResponseEntity.notFound().build();

// 500 Internal Server Error
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
```

## 3. Consistent Response Format

```java
public class ApiResponse<T> {
    private boolean success;
    private String message;
    private T data;
    private long timestamp;
    
    // Success response
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "Success", data, System.currentTimeMillis());
    }
    
    // Error response
    public static <T> ApiResponse<T> error(String message) {
        return new ApiResponse<>(false, message, null, System.currentTimeMillis());
    }
}

// Usage
@GetMapping("/users/{id}")
public ResponseEntity<ApiResponse<User>> getUser(@PathVariable Long id) {
    User user = userService.findById(id);
    return ResponseEntity.ok(ApiResponse.success(user));
}
```

## 4. Pagination

```java
@GetMapping("/products")
public Page<Product> getProducts(
    @RequestParam(defaultValue = "0") int page,
    @RequestParam(defaultValue = "10") int size
) {
    Pageable pageable = PageRequest.of(page, size);
    return productRepository.findAll(pageable);
}
```

## 5. API Versioning

```java
@RestController
@RequestMapping("/api/v1/users")
public class UserControllerV1 {
    // Version 1 endpoints
}

@RestController
@RequestMapping("/api/v2/users")
public class UserControllerV2 {
    // Version 2 with improvements
}
```
''',
            'order': 3
        },
        {
            'title': 'Logging & Exception Handling',
            'content': '''# Logging & Exception Handling

## Logging with SLF4J

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class UserService {
    private static final Logger logger = LoggerFactory.getLogger(UserService.class);
    
    public User createUser(UserDTO dto) {
        logger.info("Creating user with email: {}", dto.getEmail());
        
        try {
            User user = new User();
            user.setEmail(dto.getEmail());
            User saved = userRepository.save(user);
            
            logger.info("User created successfully: ID={}", saved.getId());
            return saved;
            
        } catch (DataIntegrityViolationException e) {
            logger.error("Failed to create user: Duplicate email", e);
            throw new EmailExistsException("Email already exists");
        } catch (Exception e) {
            logger.error("Unexpected error while creating user", e);
            throw new RuntimeException("User creation failed");
        }
    }
}
```

## Log Levels

```java
logger.trace("Detailed trace information");  // Most detailed
logger.debug("Debug information");
logger.info("Informational message");  // Default
logger.warn("Warning message");
logger.error("Error message");  // Production errors
```

## Global Exception Handler

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException ex) {
        logger.warn("User not found: {}", ex.getMessage());
        ErrorResponse error = new ErrorResponse(404, ex.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(EmailExistsException.class)
    public ResponseEntity<ErrorResponse> handleEmailExists(EmailExistsException ex) {
        logger.warn("Email already exists: {}", ex.getMessage());
        ErrorResponse error = new ErrorResponse(400, ex.getMessage());
        return ResponseEntity.badRequest().body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(Exception ex) {
        logger.error("Unexpected error occurred", ex);
        ErrorResponse error = new ErrorResponse(500, "Internal server error");
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

## application.properties

```properties
# Logging configuration
logging.level.root=INFO
logging.level.com.example.demo=DEBUG
logging.file.name=logs/application.log
logging.pattern.console=%d{yyyy-MM-dd HH:mm:ss} - %msg%n
```
''',
            'order': 4
        },
        {
            'title': 'Deployment & Common Mistakes',
            'content': '''# Deployment & Common Mistakes

## Deployment Basics

### 1. Build JAR File

```bash
mvn clean package
# Creates: target/myapp.jar
```

### 2. Run JAR

```bash
java -jar target/myapp.jar
```

### 3. Environment Variables

```bash
# Set database URL for production
export SPRING_DATASOURCE_URL=jdbc:mysql://prod-db:3306/mydb
export SPRING_DATASOURCE_PASSWORD=prod_password

java -jar myapp.jar
```

## application-prod.properties

```properties
server.port=8080
spring.datasource.url=${DB_URL}
spring.datasource.username=${DB_USERNAME}
spring.datasource.password=${DB_PASSWORD}
spring.jpa.hibernate.ddl-auto=validate
logging.level.root=WARN
```

## Docker Deployment

```dockerfile
FROM eclipse-temurin:17-jdk-alpine
COPY target/myapp.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```

## Common Beginner Mistakes

### 1. Not Using DTOs

```java
// ❌ Bad (exposing entity directly)
@PostMapping
public User create(@RequestBody User user) {
    return userRepository.save(user);
}

// ✅ Good (using DTO)
@PostMapping
public UserResponse create(@RequestBody UserDTO dto) {
    User user = userService.create(dto);
    return new UserResponse(user);
}
```

### 2. Storing Passwords in Plain Text

```java
// ❌ Never do this
user.setPassword(dto.getPassword());

// ✅ Always hash
user.setPassword(passwordEncoder.encode(dto.getPassword()));
```

### 3. Not Handling Null Values

```java
// ❌ Bad
User user = userRepository.findById(id).get();  // Throws exception if not found

// ✅ Good
User user = userRepository.findById(id)
    .orElseThrow(() -> new UserNotFoundException("User not found"));
```

### 4. Missing Validation

```java
// ❌ Bad
@PostMapping
public User create(@RequestBody User user) {
    return userService.save(user);
}

// ✅ Good
@PostMapping
public User create(@Valid @RequestBody UserDTO dto) {
    return userService.save(dto);
}
```

### 5. Not Using Transactions

```java
// ✅ Good
@Transactional
public void transferMoney(Long fromId, Long toId, Double amount) {
    accountService.debit(fromId, amount);
    accountService.credit(toId, amount);
    // Both operations succeed or both fail
}
```

## Key Takeaways

✅ Use environment variables for secrets
✅ Enable production logging
✅ Use DTOs for API requests/responses
✅ Always hash passwords
✅ Handle exceptions gracefully
✅ Use @Transactional for critical operations
✅ Validate all user input
✅ Test before deploying!
''',
            'order': 5
        }
    ]
    
    for topic_data in stage5_topics:
        Topic.objects.create(stage=stage5, **topic_data)
    
    print(f"✅ Stage 5: {stage5.title} - {len(stage5_topics)} topics")
    
    # Update roadmap stats
    roadmap.update_stats()
    
    print("\n" + "="*60)
    print(f"✅ COMPLETE: Java Backend Development Roadmap!")
    print(f"   Total Stages: 5")
    print(f"   Total Topics: 25")
    print(f"   Status: Ready for students!")
    print("="*60)

if __name__ == '__main__':
    add_remaining_stages()
