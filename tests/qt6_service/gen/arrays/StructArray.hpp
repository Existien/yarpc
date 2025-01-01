/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
 *   Object: StructArray
 *   Template: qt6/struct_header.j2
 */

#pragma once
#include <QObject>
#include <QDBusArgument>
#include <QDBusMessage>
#include <qqmlintegration.h>

namespace gen::arrays {

/**
 * @brief A struct containing arrays
 */
struct StructArray {
    Q_GADGET
    /**
     * @brief some numbers
     */
    Q_PROPERTY(QList<QList<uint>> numbers MEMBER numbers)
public:
    /**
     * @brief some numbers
     */
    QList<QList<uint>> numbers;
};

/**
 * @brief Marshalls a StructArray into a QDBusArgument.
 *
 * @param argument the argument to marshall into
 * @param object the object to marshall
 *
 * @returns QDBusArgument the argument containing the marshalled object (same as argument)
 */
QDBusArgument &operator<<(QDBusArgument &argument, const StructArray &object);

/**
 * @brief Demarshalls a StructArray from a QDBusArgument.
 *
 * @param argument the argument to demarshall from
 * @param object the object to demarshall
 *
 * @returns QDBusArgument the argument containing the marshalled object (same as argument)
 */
const QDBusArgument &operator>>(const QDBusArgument &argument, StructArray &object);

bool operator!=(const StructArray &lhs, const StructArray &rhs);

bool operator!=(const QList<StructArray> &lhs, const QList<StructArray> &rhs);

/**
 * @brief Factory to create StructArray objects in QML.
 */
class StructArrayFactory : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON
public:
    /**
     * @brief Create a StructArray object.
     *
     * @param numbers some numbers
     */
    StructArray create (
        QList<QList<uint>> numbers
    ) const;

    /**
     * @brief Create a StructArray object.
     *
     * @param numbers some numbers
     */
    Q_INVOKABLE StructArray create (
        QVariant numbers
    ) const;
};

}

Q_DECLARE_METATYPE(gen::arrays::StructArray)