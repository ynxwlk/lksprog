using System;
using System.Collections.Generic;
using System.Text;

using Autodesk.AutoCAD;
using Autodesk.AutoCAD.Geometry;
using Autodesk.AutoCAD.Runtime;
using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.EditorInput;
using Autodesk.AutoCAD.Colors;
using DBTransMan = Autodesk.AutoCAD.DatabaseServices.TransactionManager;

namespace HelloArx
{
    public class Class1
    {
        //加载实体到数据库
        public static ObjectId AppendEntity(Entity ent)
        {
            Database db = HostApplicationServices.WorkingDatabase;
            ObjectId entId;
            using (Transaction trans = db.TransactionManager.StartTransaction())
            {
                BlockTable bt = (BlockTable)trans.GetObject(db.BlockTableId, OpenMode.ForRead);
                BlockTableRecord btr = (BlockTableRecord)trans.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForWrite);
                entId = btr.AppendEntity(ent);
                trans.AddNewlyCreatedDBObject(ent, true);
                trans.Commit();

            }
            return entId;
        }
        //由两点创建直线
        public static ObjectId AddLine(Point3d startPt, Point3d endPt)
        {

            Line ent = new Line(startPt, endPt);
            ObjectId entId = AppendEntity(ent);
            return entId;
        }
    }
}