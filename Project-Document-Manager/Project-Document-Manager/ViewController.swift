//
//  ViewController.swift
//  Project-Document-Manager
//
//  Created by Tony Cioara on 1/22/18.
//  Copyright © 2018 Tony Cioara. All rights reserved.
//

import UIKit

struct ImageCollection: Codable {
    var collectionName: String
    var zippedImagesURL: String
    
    enum CodingKeys: CodingKey, String {
        case collectionName = "collection_name"
        case zippedImagesURL = "zipped_images_url"
    }
}

class ViewController: UIViewController {
    
    var imageCollections: [ImageCollection]?

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        Network.instance.fetch() { (data) in
            if let jsonImageCollections = try? JSONDecoder().decode([ImageCollection].self, from: data) {
                self.imageCollections = jsonImageCollections
                print(self.imageCollections!)
                
            }
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

