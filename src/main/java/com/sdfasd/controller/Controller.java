package com.sdfasd.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import com.sdfasd.service.Service;

@RestController
public class Controller {

  @Autowired
  private Service service;

  public String getData() {
    return service.getData();
  }
  
  public void setData(String data) {
    service.setData(data);
  }
  
  public void processData() {
    service.processData();
  }
  
  public void deleteData() {
    service.deleteData();
  }
}