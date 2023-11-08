using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class HandsTracking : MonoBehaviour
{
    public UDPReceive udpReceive;
    public GameObject[] rightHandPoints;
    public GameObject[] leftHandPoints;

    // Start is called before the first frame update
    void Start()
    {
        
    }


    // Update is called once per frame
    void Update()
    {
        string data = udpReceive.data;

        data = data.Remove(0, 1);
        data = data.Remove(data.Length-1, 1);
        // print(data);
        string[] points = data.Split(',');
        print(points[1]);

        //1        2*3      3*3
        //x1,y1,z1,x2,y2,z2,x3,y3,z3

        if (int.Parse(points[0]) == 1 && int.Parse(points[1]) == 1)
        {

            for (int i = 0; i<21; i++)
            {

                float x = 3 - float.Parse(points[i * 3 + 2]) / 100;
                float y = float.Parse(points[i * 3 + 3]) / 100;
                float z = float.Parse(points[i * 3 + 4]) / 100;

                rightHandPoints[i].transform.localPosition = new Vector3(x, y, z);

            }
        }

        else if (int.Parse(points[0]) == 1 && int.Parse(points[1]) == 2)
        {

            for (int i = 0; i<21; i++)
            {

                float x = 3 - float.Parse(points[i * 3 + 2]) / 100;
                float y = float.Parse(points[i * 3 + 3]) / 100;
                float z = float.Parse(points[i * 3 + 4]) / 100;

                leftHandPoints[i].transform.localPosition = new Vector3(x, y, z);

            }
        }

        else if (int.Parse(points[0]) == 2)
        {
            for (int i = 0; i<21; i++)
            {

                float x1 = 3 - float.Parse(points[i * 3 + 2]) / 100;
                float y1 = float.Parse(points[i * 3 + 3]) / 100;
                float z1 = float.Parse(points[i * 3 + 4]) / 100;

                float x2 = 3 - float.Parse(points[i * 3 + 65]) / 100;
                float y2 = float.Parse(points[i * 3 + 66]) / 100;
                float z2 = float.Parse(points[i * 3 + 67]) / 100;

                rightHandPoints[i].transform.localPosition = new Vector3(x1, y1, z1);
                leftHandPoints[i].transform.localPosition = new Vector3(x2, y2, z2);

            }
        }
        
    }
}
