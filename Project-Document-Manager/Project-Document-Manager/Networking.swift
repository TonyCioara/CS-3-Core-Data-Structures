//
//  Networking.swift
//  Project-Document-Manager
//
//  Created by Tony Cioara on 1/22/18.
//  Copyright © 2018 Tony Cioara. All rights reserved.
//

import Foundation

class Network {
    static let instance = Network()
    
    let fullPath = "https://s3-us-west-2.amazonaws.com/mob3/image_collection.json"
    let session = URLSession.shared
    
    func fetch(completion: @escaping (Data) -> Void) {
        let pathURL = URL(string: fullPath)
        var request = URLRequest(url: pathURL!)
        
        request.httpMethod = "GET"
        
        session.dataTask(with: request) { (data, resp, err) in
            
            if let data = data {
                completion(data)
            }
        }.resume()
    }
}
