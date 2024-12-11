package com.example.ecsspringboot;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/")
public class Controller {
    
    @GetMapping("/hello")
    public String getHello() {
        return "Hello World";
    }

    @GetMapping("/message/{msg}")
    public String getMessage(@PathVariable String msg) {
        return "your msg is "+msg;
    }
}
